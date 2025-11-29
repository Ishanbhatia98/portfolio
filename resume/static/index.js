

const canvas = document.getElementById('Matrix');
const context = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;


const katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン';
const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const nums = '0123456789';

const alphabet = katakana + latin + nums;


const fontSize = 16;
const columns = canvas.width/fontSize;


const rainDrops = [];

// let paused = false;

window.paused = false;

for( let x = 0; x < columns; x++ ) {
    rainDrops[x] = 1;
}


const draw = () => {
    if(paused) return;
    context.fillStyle = 'rgba(0, 0, 0, 0.05)';
    context.fillRect(0, 0, canvas.width, canvas.height);

    context.fillStyle = '#0F0';
    context.font = fontSize + 'px monospace';

    for(let i = 0; i < rainDrops.length; i++)
    {
        if(paused) return;
        const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
        context.fillText(text, i*fontSize, rainDrops[i]*fontSize);

        if(rainDrops[i]*fontSize > canvas.height && Math.random() > 0.975){
            rainDrops[i] = 0;
        }
        rainDrops[i]++;
    }
};

setInterval(draw, 45);

// need to add abutton to pause and unpause the effect
const toggleBtn = document.getElementById('toggleMatrix');

toggleBtn.addEventListener('click', () => {
    paused = !paused;

    // Update icon
    toggleBtn.textContent = window.paused ? '▶️' : '⏸';

    if (!paused) {
        draw();
    }
})