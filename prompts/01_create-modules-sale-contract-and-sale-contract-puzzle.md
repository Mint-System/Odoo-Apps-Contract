---
title: "Create Modules Sale Contract and Sale Contract Puzzle"
state: draft
date_completed: YYYY-MM-DD
model:
input_tokens:
---

# Run 01

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

### Sale Contract

I have initialized the module `sale_contract`. This module depends on:
sale_start_end_dates, sale_substate, sale_order_type

Add a new tab "Contract" to the sale order form. I have prepared
`addons/contract/sale_contract/views/sale_order.xml`.

Move the `type_id`, `default_start_date` and `default_end_date` to this tab.

Add a data xml for sale order type: "Framework Agreement", "Individual Contract"

Then add a new field `sale.order:parent_contract_id many2one sale.order` and
`sale.order:child_contract_ids one2many sale.order`. Show the `parent_contract_id` in
the "Contract" tab. Add a smart button for `child_contract_ids` othe sale order form.

### Sale Contract Puzzle

I have initialized the module `sale_contract_puzzle`. This module depends on:
sale_contract, fs_folder_webdav.

The goal of this module is make an integration with Nextcloud via webdav.

First the module creates `fs.storage` data entry with the noupdate flag enabled and
these values:

- name: `Nextcloud`
- code: `nextcloud`
- directory path: `/remote.php/dav/files/admin/Odoo`
- options: `{"base_url": "https://cloud.example.com", "auth": ["username", "password"]}`

Then it adds a field `sale.order:file_contract_id FSFile`. This filetype is defined in
`oca/storage/fs_file/fields.py`. The module `fs_file` is in the dependency tree.

Show this field in the `contracts` tab.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker Set frontmatter state to completed and update date and model.
