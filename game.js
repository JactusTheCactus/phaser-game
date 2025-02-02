var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);

function preload() {
    this.load.image('logo', 'https://phaser.io/content/tutorials/making-your-first-phaser-3-game/logo.png');
}

function create() {
    this.add.image(400, 300, 'logo');
}

function update() {
    // Game loop logic
}
