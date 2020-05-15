def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1    
    elif h < window:
        return 0
    elif bounce * h > window:
        return 2 + bouncingBall(bounce*h, bounce, window)
    elif h > window:
        return 1