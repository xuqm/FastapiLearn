# coding=utf-8

import uvicorn

if __name__ == '__main__':
    uvicorn.run(app="part5.main:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run(app="part4.main:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run(app="part3.main:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run(app="part2.main:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run(app="part1.main:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run(app="application.main:app", host="127.0.0.1", port=8000, reload=True)
