# AGENTS.md — Deep CBM Knowledge Base

## Permanent Rules

1. GitHub (`oncalemcnealdv3896-afk/Deep_CBM_Knowledge_Base`) and `00_Master/Deep_CBM_Latest.xlsx` are the single source of truth.
2. Daily tasks MUST use `python scripts/daily_ingest.py` (preflight → apply → validate).
3. NEVER manually edit generated files: index CSVs, JSONL, RIS, BibTeX, QC reports, increment files.
4. Always run: `preflight` → `apply` → `validate`. Never skip steps.
5. If `validate` fails, DO NOT commit. Fix errors first.
6. NEVER modify:
   - `08_User/`
   - `00_Master/source/`
   - `00_Master/workbook_archive/`
   - Historical snapshots
   - Historical increment directories
7. Output only the run summary (status, counts, IDs, errors/warnings). Do not expand full records.
8. Do NOT re-search the web. Only access candidate official URLs when local dedup is ambiguous.
9. Provisional IDs from Daily Briefs are NOT final IDs. Always re-assign from current master state.
10. Silent on success; expand only errors on failure.

## Daily Command

```bash
BRIEF=09_Daily_Brief/YYYY-MM-DD/Deep_CBM_daily_brief_YYYYMMDD.md
RUN=09_Daily_Brief/YYYY-MM-DD/codex_run

python scripts/daily_ingest.py preflight --brief "$BRIEF" --run-dir "$RUN"
# read $RUN/preflight_summary.json
# if action=apply:
python scripts/daily_ingest.py apply --manifest "$RUN/candidate_manifest.json" --run-dir "$RUN"
python scripts/daily_ingest.py validate --run-dir "$RUN"
# read $RUN/run_summary.json
# commit only if status=success, errors=[], protected_paths_modified=false
```
