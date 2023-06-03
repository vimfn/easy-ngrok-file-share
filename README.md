# Share Files with Friends Using Flask and ngrok

This is a simple Flask app that allows you to download a file from your local machine using ngrok to create a public URL for the app.

## Prerequisites

1. Clone this repository to your local machine.
2. Create and activate a new virtual environment using the command

```bash
python3 -m venv env && source env/bin/activate
```

3. Install the required packages using the command

```bash
pip install -r requirements.txt
```

4. Copy the `.env.example` file in project root and rename it to `.env` and fill your [ngrok token](https://dashboard.ngrok.com/get-started/your-authtoken):

```bash
ngrok_token=YOUR_TOKEN_HERE
```

Run the app using the command `python share.py <file_path>`.

5. Once the app is running, you'll see a ngrok URL in the console. Share this URL with your friends to allow them to download the file.

## Troubleshooting

If you encounter any issues while using the app, try the following:

- Make sure you've installed all the required packages listed in requirements.txt.
- Check that your ngrok authentication token is correct and has been added to the .env file correctly.
- If you're having trouble sharing the ngrok URL with your friends, try opening the URL in your own browser to make sure it's working correctly.
