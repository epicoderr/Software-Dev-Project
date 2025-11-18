sequence Diagram

    participant Main
    participant HKLLaitehallinto
    participant Lataajalaite as rautatietori
    participant Lukijalaite as ratikka6
    participant Lukijalaite as bussi244
    participant Kioski as lippu_luukku
    participant Matkakortti as kallen_kortti

    Main->>HKLLaitehallinto: __init__()
    Main->>Lataajalaite: uusi Lataajalaite()
    Main->>Lukijalaite: uusi Lukijalaite() (ratikka6)
    Main->>Lukijalaite: uusi Lukijalaite() (bussi244)

    Main->>HKLLaitehallinto: lisaa_lataaja(rautatietori)
    Main->>HKLLaitehallinto: lisaa_lukija(ratikka6)
    Main->>HKLLaitehallinto: lisaa_lukija(bussi244)

    Main->>Kioski: uusi Kioski()
    Main->>Kioski: osta_matkakortti("Kalle")
    Kioski->>Matkakortti: __init__("Kalle")
    Kioski-->>Main: kallen_kortti

    Main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
    rautatietori->>kallen_kortti: kasvata_arvoa(3)

    Main->>ratikka6: osta_lippu(kallen_kortti, 0)
    ratikka6->>kallen_kortti: vahenna_arvoa(1.5)

    Main->>bussi244: osta_lippu(kallen_kortti, 2)
    bussi244->>kallen_kortti: vahenna_arvoa(3.5)
