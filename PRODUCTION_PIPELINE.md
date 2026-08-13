# Synthera Production Pipeline for SYN-P001

Trigger: Command Center receives proficiency PASS.

Flow:
1. Unlock production.
2. Discover existing Drive and GitHub assets for the current lesson.
3. Classify each requirement as VALID, PARTIAL, STALE, MISSING, or NOT_REQUIRED.
4. Adopt valid assets, complete partial assets, review stale assets, create missing assets, and skip assets that are not required.
5. Send the approved lesson package and reconciled asset inventory to Content Studio and Proof of Work.
6. Content Studio builds only required missing or approved replacement public-learning assets and posting copy.
7. Proof of Work builds only required missing or approved replacement technical documentation and evidence.
8. Store new content assets in the configured Drive location.
9. Store new technical artifacts in the configured GitHub location.
10. Update canonical operational state and tracker.
11. Return both handoffs to Command Center.
12. Command Center verifies required outputs.
13. Mark Production Complete when all required lesson-type outputs are satisfied.
14. Publishing is a separate state and may occur after Production Complete.

EJJoftheCloud v1 media policy:
- Required public output: the main non-video educational post/carousel and its posting copy.
- Short-form vertical video is optional and does not block Production Complete.
- Optional short-form video may later be distributed to Instagram Reels, TikTok, YouTube Shorts, or other platforms.
- GitHub documentation, labs, proof, architecture, and troubleshooting remain conditional on lesson requirements.

Failure behavior:
- Missing required input: stop the affected branch and report blocker.
- Integration failure: preserve completed work and keep required unfinished work incomplete.
- Conflicting state: canonical operational state wins; flag discrepancy for correction.
- Existing valid human-approved assets are preserved rather than regenerated.
