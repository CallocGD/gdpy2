# GDPY2
Will be Fixing Everything Wrong with GDPY and improve upon it. This will be the ultimate module to replace gdpy and eventually provide gd programmers of all backgrounds something to use. 

## ALL Planned Features
- GD Client that can be easy configured around with the Boomlings server or to be pointed at Other GDPS Servers 
- GD Client Will have proper HTTP, SOCKS4, SOCKS5 Support
- Aiohttp for everything
- Robdantic for objects and for Converting strings to Objects and vice-versa
- Will be Easy to reverse engineer and learn how everything inside the library works
- A Parser and Writer for Robtop Strings in different Dataclasses
- IntDict for helping the Paser and Writer Set Robdatic Fileds
- Clean Event Listeners (as well as typehinting things)
- Comment Bots (Not Hiding anything from you, This is the big plan) 
- A Fixable & Repairable API Whenever Robtop Moves Shit around which our end easy to maintain and Improve upon. 
- proper context managers on Client and lower portions of code. 
- Cloudflare Error Handling (I hate those stupid things)
- Built-in Base64 encode/decoders
- Propper encoding (no more encode and decode functions (it's annoying))

## Progress
- [x] Parser/Writer (Completed)
- [x] IntDict (Completed)
- [ ] Robdantic-Core (In Progress, The other tools were required first)
- [ ] Robdantic-attrs backend
- [ ] Robdantic-sqlalchemy backend
- [ ] HTTP Client
- [ ] Aiohttp Server setup for running a simple gdps server with premade databases
- [ ] Resoponse Models (Requires Robdantic Attrs)
- [ ] A Proper GDPS Server (Requires Robdantic-sqlalchemy)
- [ ] A Small Crypto Module (working on typehinting chks in a friendly way to people unfamiliar with this)
- [ ] A HTTP Configuration dataclass for swapping between http endpoints or gdps servers.
- [ ] Event Listeners
- [ ] Making the Entire library Typehint-friendly for pyright to read


