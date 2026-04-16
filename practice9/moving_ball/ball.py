class Ball:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.radius = 25
        self.speed = 20

    def move(self, dx, dy, width, height):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= width - self.radius:
            self.x = new_x
        if self.radius <= new_y <= height - self.radius:
            self.y = new_y