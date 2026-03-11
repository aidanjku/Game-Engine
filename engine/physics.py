def apply_gravity(sprite, gravity=0.1):
    sprite.vy += gravity
    sprite.rect.y += sprite.vy

def collide(sprite, platforms):
    for p in platforms:
        if sprite.rect.colliderect(p.rect):
            # simple "land on top" collision
            if sprite.vy > 0:
                sprite.rect.bottom = p.rect.top
                sprite.vy = 0