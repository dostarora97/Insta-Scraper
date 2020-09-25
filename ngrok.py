from pyngrok import ngrok
from main import run

def main():
    public_url = ngrok.connect(5000)
    print("Navigate to : {}".format(public_url))
    run()

    ngrok_process = ngrok.get_ngrok_process()

    try:
        # Block until CTRL-C or some other terminating event
        ngrok_process.proc.wait()
    except KeyboardInterrupt:
        print(" Shutting down NGROK server.")
        ngrok.kill()
    finally:
        ngrok.kill()

if __name__ == "__main__":
    main()
