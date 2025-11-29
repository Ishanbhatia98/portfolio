import * as THREE from 'https://unpkg.com/three@0.126.1/build/three.module.js';
import { OrbitControls } from 'https://unpkg.com/three@0.126.1/examples/jsm/controls/OrbitControls.js';

window.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('three-container');

    // Renderer with transparent background
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setClearColor(0x000000, 0);
    container.appendChild(renderer.domElement);

    const scene = new THREE.Scene();

    // Camera
    const camera = new THREE.PerspectiveCamera(
        50,
        container.clientWidth / container.clientHeight,
        1,
        4000
    );
    camera.position.z = 1000;

    // Controls (optional)
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.1;

    // Video setup
    const video = document.createElement('video');
    video.src = 'https://threejs.org/examples/textures/kinect.webm'; // same as official example
    video.crossOrigin = 'anonymous';
    video.loop = true;
    video.muted = true;
    video.play();

    const videoTexture = new THREE.VideoTexture(video);
    videoTexture.minFilter = THREE.NearestFilter;
    videoTexture.magFilter = THREE.NearestFilter;
    videoTexture.format = THREE.RGBFormat;

    // Geometry
    const width = 640;
    const height = 480;
    const geometry = new THREE.BufferGeometry();
    const vertices = new Float32Array(width * height * 3);

    for (let i = 0, j = 0; i < vertices.length; i += 3, j++) {
        vertices[i] = j % width;
        vertices[i + 1] = Math.floor(j / width);
        vertices[i + 2] = 0; // initial z
    }

    geometry.addAttribute('position', new THREE.BufferAttribute(vertices, 3));

    // Material with shaders
    const material = new THREE.ShaderMaterial({
        uniforms: {
            map: { value: videoTexture },
            width: { value: width },
            height: { value: height },
            pointSize: { value: 2 },
            zOffset: { value: 1000 },
        },
        vertexShader: `
            uniform sampler2D map;
            uniform float width;
            uniform float height;
            uniform float pointSize;
            uniform float zOffset;
            varying vec2 vUv;
            void main() {
                vUv = vec2(position.x / width, 1.0 - (position.y / height));
                vec4 color = texture2D(map, vUv);
                float depth = (color.r + color.g + color.b) / 3.0;
                vec4 mvPosition = modelViewMatrix * vec4(
                    (position.x - width / 2.0),
                    -(position.y - height / 2.0),
                    -depth * 1000.0 + zOffset,
                    1.0
                );
                gl_PointSize = pointSize;
                gl_Position = projectionMatrix * mvPosition;
            }
        `,
        fragmentShader: `
            uniform sampler2D map;
            varying vec2 vUv;
            void main() {
                vec4 color = texture2D(map, vUv);
                gl_FragColor = vec4(color.rgb, 0.6);
            }
        `,
        transparent: true,
    });

    const particles = new THREE.Points(geometry, material);
    scene.add(particles);

    // Handle resize
    window.addEventListener('resize', () => {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });

    // // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        // Skip rendering if paused
        if (window.paused) return;
        // Update video texture
        if (video.readyState >= video.HAVE_CURRENT_DATA) {
            videoTexture.needsUpdate = true;
        }

        controls.update();
        renderer.render(scene, camera);
    }

    animate();

});