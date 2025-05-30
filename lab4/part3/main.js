// setup canvas

const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");

const width = (canvas.width = window.innerWidth);
const height = (canvas.height = window.innerHeight);

// function to generate random number

function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// function to generate random color

function randomRGB() {
  return `rgb(${random(0, 255)},${random(0, 255)},${random(0, 255)})`;
}

class Ball {
    constructor(x, y, velX, velY, color, size) {
      this.x = x;
      this.y = y;
      this.velX = velX;
      this.velY = velY;
      this.color = color;
      this.size = size;
    }

    draw() {
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
        ctx.fill();
      } 

      update() {
        // bounce off right and left walls
        if ((this.x + this.size) >= width || (this.x - this.size) <= 0) {
          this.velX = -this.velX;
        }
      
        // bounce off top and bottom walls
        if ((this.y + this.size) >= height || (this.y - this.size) <= 0) {
          this.velY = -this.velY;
        }
      
        // update position
        this.x += this.velX;
        this.y += this.velY;
      }
      collisionDetect() {
        for (const otherBall of balls) {
          if (!(this === otherBall)) {
            const dx = this.x - otherBall.x;
            const dy = this.y - otherBall.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
      
            if (distance < this.size + otherBall.size) {
              this.color = randomRGB();
              otherBall.color = randomRGB();
            }
          }
        }
      }
               
  }

const balls = [];

  while (balls.length < 25) {
    const size = random(10, 20);
    const ball = new Ball(
      random(0 + size, width - size),
      random(0 + size, height - size),
      random(-7, 7), 
      random(-7, 7), 
      randomRGB(),   
      size
    );
  
    balls.push(ball);
  }

  function loop() {
    ctx.fillStyle = "rgb(0 0 0 / 25%)";
    ctx.fillRect(0, 0, width, height);
  
    for (const ball of balls) {
      ball.draw();
      ball.update();
      ball.collisionDetect();
    }
    requestAnimationFrame(loop);
  }
  loop();

  
  


  




  

  
  


  
