# Yolo v8 Aim Assist
## How to set up the environment

`pip install -r requirements.txt`

if you have a cuda capable gpu, you can running the following extra command

`pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116`

## How to run the program
just run the main.py file with the following command

`python main.py`

After a few seconds, the program will start to run. You can see `Main Start` in the console.

Once you click the right mouse button, the program will start to aim at the enemy.

## How to change the settings
You can change the settings in the `args.py` file.

### Some important settings!!!:
- game_fps 
    - You should set it to match your game fps (no more than you screen refresh rate). If it's higher than your actual fps, your front sight
would jump from side to side.
- model
    - The default model is for Apex. However, you can train your own model using train.py, and switch the model using this setting.
- crop_size
    - This setting determines the portion of the screen to be detected. Too high may cause difficulty in detecting little objects.
## Note
This program is only for educational purposes. I am not responsible for any damage caused by this program.