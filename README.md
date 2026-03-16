# JackBulwark

This project provides a highly advanced, feature-rich Telegram bot built with [Pyrogram](https://docs.pyrogram.org/) for indexing media, serving results through powerful inline queries and PM filters, and providing media streaming capabilities.

## 🌟 Key Features

- **Robust Database System**: Connects to MongoDB for storing indexed media metadata. Supports **Dual Database** setups (`DATABASE_URI` and `DATABASE_URI_2`) for load balancing and backup.
- **Advanced PM Filters & UI**: Modern design featuring multi-page pagination, two-column layouts, visual separators, and built-in language filters (Tamil, Telugu, Hindi, Malayalam, Kannada, English).
- **Movie Updates Broadcaster**: Automatically announces newly indexed movies to a dedicated updates channel, enriched with IMDb metadata, audio/quality tags, and quick-access buttons.
- **Discovery / Browse Menu**: Explore content naturally via the new `/browse` menu, filtering by **Genres** and **Major Release Years**.
- **Personal Watchlist**: Save movies for later with the "⭐ Add Watchlist" button and manage them using the `/watchlist` command.
- **Trailer Integration**: Instant access to movie trailers via integrated "📹 Trailer" buttons on all search results.
- **Fast Download & Streaming**: Provides users with fast HTTP streaming links using your custom `STREAM_URL`.
- **GoFile Uploads**: Allows users to seamlessly push files straight to GoFile servers for quick mirror links.
- **Multi-Force Subscription**: Requires users to join up to two different authorization channels before accessing the bot.
- **IMDb & TMDB Integration**: Automatically fetches movie details, ratings, runtimes, and posters, formatted using customizable templates.
- **Modular Plugin System**: Clean architecture divided into modules for filtering, broadcasting, connections, and health-checks via `aiohttp` web server.

---

## ⚙️ Configuration Variables

All configuration is performed through environment variables defined in [`info.py`](info.py). 

### Essential Variables
| Variable | Description |
| --- | --- |
| `API_ID` / `API_HASH` | Telegram API credentials obtained from [my.telegram.org](https://my.telegram.org/). |
| `BOT_TOKEN` | Bot token obtained from [@BotFather](https://t.me/BotFather). |
| `SESSION` | Session name used by Pyrogram. |
| `DATABASE_URI` | Primary MongoDB connection string. |
| `DATABASE_NAME` / `COLLECTION_NAME` | Primary database and collection names. |
| `ADMINS` | Space-separated list of User IDs with admin access to the bot. |
| `CHANNELS` | Space-separated list of channel IDs where the bot should index files. |
| `LOG_CHANNEL` | Channel ID for logging system events and new user interactions. |

### Secondary Database (Optional)
| Variable | Description |
| --- | --- |
| `DATABASE_URI_2` | Secondary MongoDB connection string. |
| `DATABASE_NAME_2` / `COLLECTION_NAME_2` | Secondary database and collection names. |

### Access & Force Subscription (Optional)
| Variable | Description |
| --- | --- |
| `AUTH_USERS` / `AUTH_GROUPS` | Strict access control to restrict usage to specific users or groups. |
| `AUTH_CHANNEL` | Channel ID users must join to use the bot. |
| `MULTI_FORCESUB` | Enable/Disable requirement to join second channel (`True` / `False`). |
| `AUTH_CHANNEL_2` | Second channel ID users must join if multi-forcesub is enabled. |

### Optional Integrations
| Variable | Description |
| --- | --- |
| `STREAM_URL` | Your custom streaming server URL (e.g., `https://your-stream-app.com`). |
| `ENABLE_STREAM_LINK` | Toggle the display of Fast DL buttons (`True` / `False`). |
| `GOFILE_TOKEN` | API Token for authenticated GoFile uploads. |
| `ENABLE_GOFILE_LINK` | Toggle the display of GoFile upload buttons (`True` / `False`). |
| `TMDB_API_KEY` | API key from themoviedb.org for fetching metadata. |

### UI & UX Toggles
| Variable | Description |
| --- | --- |
| `IMDB` | Toggle IMDb details fetching (`True` / `False`). |
| `SPELL_CHECK_REPLY` | Toggle AI text suggestions for incorrect queries (`True` / `False`). |
| `P_TTI_SHOW_OFF` | Redirects users to PM instead of sending files directly in groups (`True` / `False`). |
| `SINGLE_BUTTON` | Display filename and size in a single button instead of two (`True` / `False`). |
| `CUSTOM_FILE_CAPTION` | Format string for media captions (`{file_caption}`, `{file_size}`, etc). |
| `IMDB_TEMPLATE` | Format string for IMDb announcement posts structure. |
| `ANNOUNCE_MOVIE_UPDATES` | Toggle auto-posting to the updates channel (`True` / `False`). |
| `MOVIE_UPDATES_CHANNEL` | Channel ID where new movie updates should be broadcasted. |

---

## 🚀 Running the Bot

1. Install all required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Populate the environment variables (e.g. locally via `.env` or system var exports).
3. Start the application:
   ```bash
   python bot.py
   ```

The bot will execute the Telegram client and simultaneously serve the `aiohttp` web application on `0.0.0.0:<PORT>` to satisfy health-checks for common cloud hosts (Heroku, Render, etc.).

### Automatic Movie Announcements
When `ANNOUNCE_MOVIE_UPDATES=True` and `MOVIE_UPDATES_CHANNEL` is defined, every newly indexed media item in the database will trigger a polished announcement enriched with IMDb data and interactive inline buttons ("Fast Download Link", "GoFile Upload").

Administrators can also manually trigger an announcement using:
```text
/post <movie name>
```

---

## 🛠 Useful Admin Commands
- `/channel` - Displays the currently indexed channels/groups.
- `/logs` - Fetches the latest system logs.
- `/delete` / `/deleteall` - Removes localized or complete indexed files.
- `/delkeyword <word>` - Bulk delete database entries matching a regex or specific keyword.
- `/detectduplicates` - Identifies and removes content-equivalent files (preserving the newest).
- `/compact` - Runs an optimization job on the MongoDB clusters.

---

## 📜 License
This project is licensed under the terms of the MIT License.
