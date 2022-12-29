import math

def line_overlaps(x1,y1,x2,y2,xx1,yy1,xx2,yy2):
    if (x2 < x1):
        buf = x1
        x1 = x2
        x2 = buf
        buf=y1
        y1=y2
        y2=buf

    if (xx2 < xx1):
        buf = xx1
        xx1 = xx2
        xx2 = buf
        buf=yy1
        yy1=yy2
        yy2=buf

    if (x2 < xx1):
        return False

    if((x1 - x2 == 0) and (xx1 - xx2 == 0)):
        if(x1 == xx1):
            if (not((max(y1, y2) < min(yy1, yy2)) or
                    min(y1, y2) > max(yy1, yy2))):
                return True
        return False

    if (x1 - x2 == 0):
        Xa = x1
        A2 = (yy1 - yy2) / (xx1 - xx2)
        b2 = yy1 - A2 * xx1
        Ya = A2 * Xa + b2
        if (xx1 <= Xa and xx2 >= Xa and min(y1, y2) <= Ya and max(y1, y2) >= Ya):
            return True
        return False

    if (xx1 - xx2 == 0):
        Xa = xx1
        A1 = (y1 - y2) / (x1 - x2)
        b1 = y1 - A1 * x1
        Ya = A1 * Xa + b1
        if (x1 <= Xa and x2 >= Xa and min(yy1, yy2) <= Ya and max(yy1, yy2) >= Ya):
            return True
        return False

    A1 = (y1 - y2) / (x1 - x2)
    A2 = (yy1 - yy2) / (xx1 - xx2)
    b1 = y1 - A1 * x1
    b2 = yy1 - A2 * xx2
    if (A1 == A2):
        return False
    Xa = (b2 - b1) / (A1 - A2)
    if ((Xa < max(x1, xx1)) or (Xa > min(x2, xx2))):
        return False
    else:
        return True
def point_in_rect1(pointX,pointY,rectX1,rectY1,rectX2,rectY2):
    if (pointX>=rectX1 and pointX<=rectX2 and pointY>=rectY1 and pointY<=rectY2):
        return True
    return False
    
def point_in_rect(pointX,pointY,element):
    rectX1=min(element.coord[0],element.coord[6])
    rectX2=max(element.coord[0],element.coord[6])
    rectY1=min(element.coord[1],element.coord[7])
    rectY2=max(element.coord[1],element.coord[7])
    if (pointX>=rectX1 and pointX<=rectX2 and pointY>=rectY1 and pointY<=rectY2):
        return True
    return False
def hurting(attack_piece,piece,owner,attack):
    if( attack_piece.overlap(piece)):
            if(owner.face):
                    if(attack[1]>owner.total_weight):
                            owner.vectX=attack[1]-owner.total_weight
            else:
                    if(attack[1]>owner.total_weight):
                            owner.vectX=-(attack[1]-owner.total_weight)
            hurting_hit(piece,owner,attack[0])
            return True
    return False

def hurting_hit(piece,owner,attack):
        piece.health-=attack
        owner.damaged()

        if(piece.health<=0):
            pass

def create_bullet_vector(x1,y1,x2,y2,power=1):
    ug = (math.acos(((x1) * x2 + (y1) * y2) / (math.sqrt((x1) * (x1) + (y1) * (y1)) * math.sqrt(x2 * x2 + y2 * y2))))
    A=[x2-x1,y2-y1]
    dl=math.sqrt(A[0]**2+A[1]**2)
    return A[0]/dl * power, A[1]/dl * power