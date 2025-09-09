from uvicorn import run


def main():
    print("Hello from web-hello-world!")
    run("web.app:app", reload=True)
    # run("web.app:app", workers=4)


if __name__ == "__main__":
    main()
