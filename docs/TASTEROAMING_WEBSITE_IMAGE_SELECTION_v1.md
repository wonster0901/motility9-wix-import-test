# TasteRoaming — approved website photography selection v1.0

Source: **TasteRoaming_MasterImages_640x480_v1.0_FINAL.zip**, internal final image master. Exactly 350 images, 640×480, WebP, no duplicate SHA-256 hashes. Original master image bytes remain unchanged. This selection is for **website presentation** only; it is not a new generated or substituted image master.

## Website subset (8 source files)

| Asset | Dish | Country | Page treatment |
| --- | --- | --- | --- |
| `TRF0003.webp` | Bibimbap | KR | Taste hero main, brand card strip |
| `TRF0011.webp` | Edomae Sushi | JP | Gallery |
| `TRF0023.webp` | Pad Thai | TH | Gallery, brand card strip |
| `TRF0029.webp` | Tacos al Pastor | MX | Taste hero secondary, gallery |
| `TRF0043.webp` | Butter Chicken | IN | Gallery |
| `TRF0045.webp` | Paella Valenciana | ES | Taste hero secondary, brand card strip |
| `TRF0049.webp` | Doro Wat | ET | Gallery |
| `TRF0050.webp` | Pastel de Nata | PT | Gallery |

The assets total ~406 KB and must be placed under `assets/tasteroaming/`; each file is an original **640×480 WebP** from the approved master. No image generated or recompressed for the website. Maintain 4:3 using CSS `aspect-ratio: 4 / 3` / `object-fit: cover` without stretching.

## Verified SHA-256
```
TRF0003.webp 358a4a12762cca41bdcf6c820724d8baee143b9ca45b7e81d673a1642cc31668
TRF0011.webp 2a119a40f57803e70f35f84e8dcc141d97f5688c327a31b1753fe4b7369627fb
TRF0023.webp d2d484a08fec731b1fd767c573da38e4a90a9560d942f492fa6322e5bd55b595
TRF0029.webp 1c3133b1515957fe6765f50a75925adae3b03c85e14c2285fee62704dafdabaf
TRF0043.webp 4766ffd1e66262436959985df37e42c350e3faadecbe0444a9ec837ffc986985
TRF0045.webp 8421306e0484f405042fd9202bd18007a3e4fb50d2c243dd6a1a2a80b726ad91
TRF0049.webp e7e3cec39e9f4429143bc8118046cacbe1e46a045a853d3ab95cb0752e822d89
TRF0050.webp a55569eba795784f98593937bf879f0bd31cc7c414fbb80628b49b92be14c121
```

## Non-production handoff package

The ChatGPT conversation contains a downloadable **`WONWINNIE_Site_Finish_Patch_v1.zip`** prepared from the PR #1 preview at base `08e49f6`, with suggested HTML/CSS changes, all 8 original images, and machine-readable manifest. The package is **not a deployed website** and is **not automatically available to Codex** unless the user attaches it or places it in Codex's working directory. Avoid overwriting newer branch edits when integrating; this is a diff/asset source.

## Required checks before accepting Codex completion
- Locate the assets in the original 350 FINAL package and compare SHA-256 byte-for-byte.
- Replace original site check's blanket no-food-images assertion with an allowlist of the eight approved assets + actual SHA hashes.
- Keep existing historical/legacy pages and legal text intact.
- Keep only the verified MOTILITY9 Google Play CTA: `https://play.google.com/store/apps/details?id=com.wonwinnie.motility9`; TasteRoaming is Coming Soon.
- Run static + actual browser/accessibility checks at 320, 375, 430, 768, 1280, 1440px and 200% text. Inspect actual 4:3 image rendering and no sideways scroll.
- Do not expose the draft TasteRoaming Privacy/Terms as final. Do not merge/publish until owner approval.

