# Using the editor

1. Click **Open XML file** or double-click a suggested file. If none exists, click **Create new profile**. A missing or malformed file is reported without changing it.
2. Select a row to see its description, evidence status and source. Double-click to edit, or click **+ Add setting** to search all documented candidates. Unreviewed values are raw text with an explicit warning; check the linked source and your engine before using them.
3. Edit or remove settings. Nothing is written yet. **Review changes** shows the serialized XML diff. Removing a value also removes a directly attached preceding XML comment; other comments remain. Removing an override may reveal another configuration layer or default.
4. Click **Save changes**. Check the target path and diff in the confirmation dialog. Existing files get an exact backup before replacement. If the source changed after opening, reload it or use **File → Save a copy**.

**File** also contains Backup and Restore. Backup copies the current on-disk file without staged changes. Save a copy exports the staged result while keeping the current editing target. Restore reviews the replacement and backs up the current file first. Backups remain until you remove them.

Use **View → Night mode** to switch color schemes. The window opens centered within the available area of the monitor under the pointer.

For extra context, choose **Tools → Select UE5 engine** and optionally **Select Unreal project**. These are not required for opening XML. A matching local engine schema can validate the staged XML; without one, compatibility is unverified. **Build check** opens a separate dialog with an editable command field. When engine and project are available, it starts with a suggested command; otherwise enter your own. A successful process does not prove the selected XML was consumed.

The app works on one selected XML profile at a time. It cannot infer the complete effective UnrealBuildTool configuration from that file. Unknown XML stays intact; serialization may change formatting, so review the diff before saving.
