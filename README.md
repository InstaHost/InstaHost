![](Images/LogoGitBG.png)

# Instahost (In Development)

Instant is a quick setup tool for generating docker-compose files. The user can select the services they want or presets to help them quickly create media servers, VPNs, and torrents. While much more is planned to be added, I hope to get these created first. This is still under development (solely by me), and if you would like to suggest a new service/feature to be added, we encourage you to create an issue. This repo does acknowledge pull requests; if you want to add a service yourself, create a docker-compose for it!

Planned features:
- Docker Compose generation
- Directory management (create required dirs and manage permissions for them)
- Support for hard linking

Supported Services:

Web Docker Manager
- Homarr (Recommended for Automated Media Server)

Automated Media Server
- Prowlarr
- Jackett
- Radarr
- Sonarr
- Lidarr
- Readarr
- Jellyseerr
- Overseerr
- Cloudsolverr

VPN
- Wireguard
- OpenVPN

WebUI Clients
- VSCode Server

WebUI Torrent Client
- qBittorrent
- Deluge
- Transmission


**In-depth documentation can be found here:**
<a href="https://instahost.github.io/instahostdocs.github.io/" onclick="window.open('https://instahost.github.io/instahostdocs.github.io//', '_self');">Instahost Documentation</a>

Documentation will include the following:
- Quickstart setup
- List of presets to help simplify configuration
- Individual guides for each service
