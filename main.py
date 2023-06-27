from core.routers import app


def main():
    app.run(port=9090, debug=True)


if __name__ == '__main__':
    main()
