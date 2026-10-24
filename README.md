# The Bananas of the Caribbean

A top-down action RPG. Every banana in Europe has come alive and run off to the Caribbean, and it's up to you to peel them and eat them. After that, the trouble spreads around the world and all the way into outer space.

**Play it:** https://henrythebaby1-ops.github.io/bananas-of-the-caribbean/

## Chapters

**Part 1: The Caribbean**
1. Villages of Europe
2. Rome
3. The Atlantic (banana whales)
4. America (sky bananas)
5. The Caribbean (Captain Plantain, the Banana Boss)
6. Snake Island (the Snake King)
7. Merchant Isle (forge the diamond sword)
8. Banana Island (the Final Banana)

**Part 2: Around the world**
9. The Watermelons of Mexico
10. Canada's Favorite Apples
11. The Tangerines of China (the Tangerine Dragon)
12. The Kiwis of India
13. The Grapes of France
14. The Coconuts of Hawaii
15. The Pineapples of Australia
16. The Strawberries of Japan
17. The Lemons of Egypt
18. The Mangoes of Brazil
19. The Papayas of Kenya
20. The Oranges of South Africa
21. The Frozen Plum of Antarctica

**Part 3: Outer space**
22. The Blueberries of the Moon
23. The Pomegranates of Mars
24. The Cherries of Saturn
25. The Starfruit of the Sun
26. The Durians of Venus
27. The Jackfruits of Jupiter (the wind never stops)
28. The Blue Raspberries of Neptune
29. The Figs of Pluto
30. The Black Hole (it pulls you in)

**Part 4: Beyond the universe**
31. Beyond the Universe (Fruitus Maximus, the Fruit of Everything)

## How to play

- **Computer:** WASD or arrow keys to move, J or Space to swing your sword, K to eat, Shift to dash, Q for a snack.
- **Phone:** joystick and buttons appear under the game. Turn your phone sideways for a bigger view.

Hit an enemy with your sword to peel it, then get close and eat it before the peel grows back. Bosses get furious when they're half eaten. From chapter 9 on, every chapter is a little harder than the last: enemies have more health, hit harder, move faster, and bosses attack more often.

## Play with friends

Up to 4 players can play together online. On the title screen, choose **Play with friends**:

- One person picks **Host a new game** and gets a 4-letter code.
- Friends open the same page, pick **Play with friends**, and join from the list of open games or by typing the code.

If you get knocked out, a friend can revive you by standing next to you. Online play uses [Supabase Realtime](https://supabase.com/docs/guides/realtime) to send messages between players. It doesn't store anything.

## Files

- `src/game.html`: the game source (one file, no build tools needed).
- `build.py`: turns the source into `index.html` for GitHub Pages and adds the Supabase connection. Run `python3 build.py` after editing the source.
- `index.html`: the built page that GitHub Pages serves.
