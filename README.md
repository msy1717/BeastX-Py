# BeastX-Py Library
A stable userbot base library, based on Telethon.

[![PyPI - Version](https://img.shields.io/pypi/v/BeastX-Py?style=for-the-badge)](https://pypi.org/project/BeastX-Py)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/BeastX-Py?label=DOWNLOADS&style=for-the-badge)](https://pypi.org/project/BeastX-Py)
[![The BeastX](BeastX.svg)](https://t.me/BeastX_Userbot)

## Installation
`pip install BeastX-Py`


## Usage
=> Create folders named `plugins`, `addons`, `assistant` and `resources`.<br/>
=> Add your plugins in the `plugins` folder and others accordingly.<br/>
=> Create a `.env` file with `API_ID`, `API_HASH`, `SESSION`, `REDIS_URI` & `REDIS_PASSWORD` as mandatory environment variables. Check
[`.env.sample`](https://github.com/msy1717/Beast-X/blob/main/.env.sample) for more details.<br/>
=> Run `python -m BeastX-Py` to start the bot.<br/>

### Creating plugins
- To work everywhere

```python
@beastx_cmd(
    pattern="start",
)   
async def _(e):   
    await eor(e, "BeastX Started")   
```

- To work only in groups

```python
@beastx_cmd(
    pattern="start",
    groups_only=True,
)   
async def _(e):   
    await eor(e, "BeastX Started")   
```

- Assistant Plugins 👇

```python
@asst_cmd("start")   
async def _(e):   
    await e.reply("BeastX Started")   
```

Made with 💕 by [@msy1717](https://t.me/msy1717). <br />


# License
BeastX is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)

# Credits
@TeamUltrid
@TeamBeastX
@BeastX_Userbot
