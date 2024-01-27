def bmi(w,m,nameresult):
    BMI=(w/(m*m))
    stmt=""
    if(BMI<18.5):
        g=21.8-BMI
        we=g*m*m
        stmt='Underweight {} you should gain {} kgs to maintain normal weight'.format(nameresult,we)
    elif(BMI>=18.5 and BMI<=24.9):
        stmt='Normal Weight'
    elif(BMI>=25.0 and BMI<=29.9):
        l=BMI-24.9
        we=l*m*m
        stmt='Overweight {} you should loss {} kgs to maintain normal weight'.format(nameresult,we)
    else:
        l=BMI-24.9
        we=l*m*m
        stmt='Obesity {} you should loss {} kgs to maintain normal weight'.format(nameresult,we)
    return BMI,stmt
def logic(drops,feetresult,inchresult,metersresult,cmresult,weightresult,nameresult):
    x=""
    bmires=""
    stmtres=""
    if drops == "feet and inches":
        f = float(feetresult)
        i = float(inchresult)
        if 1.5 <= f <= 9.0 :
            if 0 <= i < 12 :
                w=float(weightresult)
                if(w>=2.5 and w<=635):
                    m=(f*0.305)+(i*0.0254)
                    
                    bmires,stmtres=bmi(w,m,nameresult)
                else:
                    x="Invalid weight entered"
            else:
                x="Invalid inches entered"
        else:
            x="Invalid feet entered"
    elif drops == "meters":
        m=float(metersresult)
        if(m>=0.457 and m<=2.7432):
            w=float(weightresult)
            if(w>=2.5 and w<=635):
                bmires,stmtres=bmi(w,m,nameresult)
            else:
                x="Invalid weight entered"
        else:
            x="Invalid meters entered"
    elif drops == "centimeters":
        cm=float(cmresult)
        if(cm>=45.72 and cm<=274.32):
            w=float(weightresult)
            if(w>=2.5 and w<=635):
                m=cm*0.01
                bmires,stmtres=bmi(w,m,nameresult)
            else:
                x="Invalid weight entered"
        else:
            x="Invalid centimeters entered"
    else:
        x="WRONG ENTRY!"

    return bmires,stmtres,x     
                    
            
