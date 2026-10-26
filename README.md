# NTM Structure Ported CE

[![Download the JAR](https://img.shields.io/badge/Download-Mod%20JAR-brightgreen?style=for-the-badge)](https://github.com/BailieByrne/NTM-Structures/raw/refs/heads/main/NTMstructure-1_12_2-2_0_2-CE.jar)

An NTM Structures compatibility port for NTM Community Edition on Minecraft
1.12.2. Block references have been remapped for NTM-CE 2.6.x.

Version 2.0.2-ce fixes missing colored concrete and flower blocks in structure
templates, the bunker that selected the wrong template, and machinery parts that
could protrude from the hangar and bunker builds. These changes affect newly
generated structures; structures already placed in a world remain as they are.

Explore a post-apocalyptic world filled with abandoned bunkers, military
checkpoints, command posts, wrecked vehicles and ships, radioactive sites,
mines, and other structures. Locations appear across different biomes and
offer places to explore and resources to discover.

## Original mod

This port is based on [HBM/NTM Structure on CurseForge](https://www.curseforge.com/minecraft/mc-mods/hbm-ntm-structure-1-12-2).

[![Submit an issue](https://img.shields.io/badge/Report-Issues-blue?style=for-the-badge)](https://github.com/BailieByrne/NTM-Structures/issues/new)

Please [submit issues here](https://github.com/BailieByrne/NTM-Structures/issues/new)
to report bugs, crashes, or other problems.

## Requirements

- Minecraft 1.12.2
- Minecraft Forge
- NTM Community Edition 2.6.x (the `hbm` dependency)

## Packaging

The unpacked `assets`, `net`, and metadata files match the included JAR.
Run `python tools/build_jar.py` to rebuild it after changing those files.

## Credits

- Original structures: AliyKorol and the other contributing builders
- CE compatibility port: BailieByrne

This project is not an official release of NTM Community Edition. The source,
resources, and included structures are All Rights Reserved by their respective
copyright holders; see [LICENSE](LICENSE).
