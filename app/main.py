from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates
from typing import Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")



templates = Jinja2Templates(directory="templates")



@app.get("/problem/7bd5274305fc374146fa52886668697b")
async def problem1(request: Request):
    return templates.TemplateResponse("problem1.html", {"request": request})
   
@app.post("/problem/42dfee3aa6bafe1beb7d128cc8bce485")
async def problem2(request: Request, user_answer: str = Form(None)):
    if user_answer == '09:24':
        return templates.TemplateResponse("problem2.html", {"request": request})
    else:
        return templates.TemplateResponse("problem1.html", {"request": request})

@app.post("/problem/30f201743c2b0c886d8cc8b6b29db140")
async def problem3(request: Request, user_answer: str = Form(None)):
    if user_answer == '초록색':
        return templates.TemplateResponse("problem3.html", {"request": request})
    else:
        return templates.TemplateResponse("problem2.html", {"request": request})

@app.post("/problem/38fc6694b92e7eaad37c088ed8599377")
async def problem3(request: Request, user_answer: str = Form(None)):
    if user_answer == '1':
        return templates.TemplateResponse("problem3-1.html", {"request": request})
    if user_answer == '2':
        return templates.TemplateResponse("problem3-2.html", {"request": request})
    else:
        return templates.TemplateResponse("problem3.html", {"request": request})

@app.post('/problem/541aadd9accadb1b5757a867e1b97186')
async def problem4(request: Request, user_answer: str = Form(None)):
    if user_answer == "start":
        return templates.TemplateResponse("problem1.html", {"request": request})
    else:
        return templates.TemplateResponse("problem3-1.html", {"request": request})

@app.post('/problem/e0e0aaa7f19ccaf4f49598f3059eaebb')
async def problem5(request: Request, user_answer: str = Form(None)):
    if user_answer == 'open':
        return templates.TemplateResponse("problem4.html", {"request": request})
    else:
        return templates.TemplateResponse("problem3-2.html", {"request": request})

@app.post('/problem/48f0451642fac41729a383822aaa8dae')
async def problem6(request: Request, user_answer: str = Form(None)):
    if user_answer == 'halloween@asleep.ai':
        return templates.TemplateResponse("problem5.html", {"request": request})
    else:
        return templates.TemplateResponse("problem4.html", {"request": request})

@app.post('/problem/bbb795627678d1e76c31869ba885283f')
async def problem7(request: Request, user_answer: str = Form(None)):
    if user_answer == '전화벨':
        return templates.TemplateResponse("problem6.html", {"request": request})
    else:
        return templates.TemplateResponse("problem5.html", {"request": request})

@app.post('/problem/6e61aa27e995834984a4bc1c12d254a1')
async def problem8(request: Request, user_answer: str = Form(None)):
    if user_answer == '1678943489760214':
        return templates.TemplateResponse("problem7.html", {"request": request})
    else:
        return templates.TemplateResponse("problem6.html", {"request": request})

@app.get('/problem/nuy')
async def purple(request: Request):
    return templates.TemplateResponse("purple.html", {"request": request})

@app.post('/problem/bb7aedfa61007447dd6efaf9f37641e3')
async def purpleA(request: Request, user_answer: str = Form(None)):
    if user_answer=='초':
        return templates.TemplateResponse("purpleA.html", {"request": request})
    else:
        return templates.TemplateResponse("purple.html", {"request": request})

@app.post('/problem/aa1faf77b4c9abf7b68459bae3d886cf')
async def purpleB(request: Request, user_answer: str = Form(None)):
    if user_answer=='거울':
        return templates.TemplateResponse("purpleB.html", {"request": request})
    else:
        return templates.TemplateResponse("purpleA.html", {"request": request})

@app.post('/problem/ade78983f234293402943e5e42f3b1d2')
async def purpleC(request: Request, user_answer:str = Form(None)):
    if user_answer=='낫':
        return templates.TemplateResponse("purpleC.html", {"request": request})
    else:
        return templates.TemplateResponse("purpleB.html", {"request": request})

@app.post('/problem/b05df563834ee82ebfc8ca886fc2889a')
async def purpleD(request: Request, user_answer: str = Form(None)):
    if user_answer=='닭':
        return templates.TemplateResponse("purpleD.html", {"request": request})
    else:
        return templates.TemplateResponse("purpleC.html", {"request": request})

@app.post('/problem/6b88fcc60fa0547ca3e2a376794d246f')
async def purpleE(request: Request, user_answer: str = Form(None)):
    if user_answer=='해골':
        return templates.TemplateResponse("purpleE.html", {"request": request})
    else:
        return templates.TemplateResponse("purpleD.html", {"request": request})

@app.get('/problem/don')
async def green(request: Request):
    return templates.TemplateResponse("green.html", {"request": request})

@app.post('/problem/bb7aedfa61007447dd6efaf9f37fkdls')
async def greenA(request: Request, user_answer: str = Form(None)):
    if user_answer=='초':
        return templates.TemplateResponse("greenA.html", {"request": request})
    else:
        return templates.TemplateResponse("green.html", {"request": request})

@app.post('/problem/aa1faf77b4c9abf7b68459bae3d8qlav')
async def greenB(request: Request, user_answer: str = Form(None)):
    if user_answer=='깃털':
        return templates.TemplateResponse("greenB.html", {"request": request})
    else:
        return templates.TemplateResponse("greenA.html", {"request": request})

@app.post('/problem/a3cd5dd1dbbc27111bef14e54e77f3e1')
async def greenC(request: Request, user_answer: str = Form(None)):
    if user_answer=='가마솥':
        return templates.TemplateResponse("greenC.html", {"request": request})
    else:
        return templates.TemplateResponse("greenB.html", {"request": request})

@app.post('/problem/0666156d9798d359df1277809b8fba65')
async def greenD(request: Request, user_answer: str = Form(None)):
    if user_answer=='쥐':
        return templates.TemplateResponse("greenD.html", {"request": request})
    else:
        return templates.TemplateResponse("greenC.html", {"request": request})

@app.post('/problem/2ef3bc384386c3a8cea4ee9f3240e7a6')
async def greenE(request: Request, user_answer: str = Form(None)):
    if user_answer=='독약':
        return templates.TemplateResponse("greenE.html", {"request": request})
    else:
        return templates.TemplateResponse("greenD.html", {"request": request})


@app.get('/problem/iaa')
async def red(request: Request):
    return templates.TemplateResponse("red.html", {"request": request})

@app.post('/problem/bda9643ac6601722a28f238714274da4')
async def redA(request: Request, user_answer: str = Form(None)):
    if user_answer=='초':
        return templates.TemplateResponse("redA.html", {"request": request})
    else:
        return templates.TemplateResponse("red.html", {"request": request})

@app.post('/problem/dec4829cd3dc67ebadee2bcf8dadc549')
async def redB(request: Request, user_answer: str = Form(None)):
    if user_answer=='옥춘당':
        return templates.TemplateResponse("redB.html", {"request": request})
    else:
        return templates.TemplateResponse("redA.html", {"request": request})

@app.post('/problem/f6c7448bd95b442b29107fd0aee18f2f')
async def redC(request: Request, user_answer: str = Form(None)):
    if user_answer=='부채':
        return templates.TemplateResponse("redC.html", {"request": request})
    else:
        return templates.TemplateResponse("redB.html", {"request": request})

@app.post('/problem/4767cf79db3c8d734fbf345e46276959')
async def redD(request: Request, user_answer: str = Form(None)):
    if user_answer=='돼지':
        return templates.TemplateResponse("redD.html", {"request": request})
    else:
        return templates.TemplateResponse("redC.html", {"request": request})

@app.post('/problem/56389c85a9a19ba307fae65f3a4cede3')
async def redE(request: Request, user_answer: str = Form(None)):
    if user_answer=='무당방울':
        return templates.TemplateResponse("redE.html", {"request": request})
    else:
        return templates.TemplateResponse("redD.html", {"request": request})

@app.get('/problem/eil')
async def blue(request: Request):
    return templates.TemplateResponse("blue.html", {"request": request})

@app.post('/problem/48d6215903dff56238e52e8891380c8f')
async def blueA(request: Request, user_answer: str = Form(None)):
    if user_answer=='초':
        return templates.TemplateResponse("blueA.html", {"request": request})
    else:
        return templates.TemplateResponse("blue.html", {"request": request})

@app.post('/problem/4a8ec8f6625ee368636427345593f58c')
async def blueB(request: Request, user_answer: str = Form(None)):
    if user_answer=='호박':
        return templates.TemplateResponse("blueB.html", {"request": request})
    else:
        return templates.TemplateResponse("blueA.html", {"request": request})

@app.post('/problem/4cb6b4e795ca7ec3feecc8c791e91d70')
async def blueC(request: Request, user_answer: str = Form(None)):
    if user_answer=='칼':
        return templates.TemplateResponse("blueC.html", {"request": request})
    else:
        return templates.TemplateResponse("blueB.html", {"request": request})

@app.post('/problem/b5cc8d3679f7a5b0fbf671a3dcacef05')
async def blueD(request: Request, user_answer: str = Form(None)):
    if user_answer=='박쥐':
        return templates.TemplateResponse("blueD.html", {"request": request})
    else:
        return templates.TemplateResponse("blueC.html", {"request": request})

@app.post('/problem/9a3e60caf47a7d5669a7c25d967b305e')
async def blueE(request: Request, user_answer: str = Form(None)):
    if user_answer=='액자':
        return templates.TemplateResponse("blueE.html", {"request": request})
    else:
        return templates.TemplateResponse("blueD.html", {"request": request})

@app.get('/ending')
async def ending(request: Request):
    return templates.TemplateResponse("ending.html", {"request": request})

@app.get('/ending2')
async def ending(request: Request):
    return templates.TemplateResponse("ending2.html", {"request": request})

@app.get('/ending3')
async def ending(request: Request):
    return templates.TemplateResponse("ending3.html", {"request": request})

@app.get('/ending4')
async def ending(request: Request):
    return templates.TemplateResponse("ending4.html", {"request": request})

@app.get('/thanks')
async def ending(request: Request):
    return templates.TemplateResponse("thanks.html", {"request": request})
