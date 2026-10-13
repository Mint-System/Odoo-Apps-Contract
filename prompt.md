---
title: "Implement Agreement CRM"
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: completed
date_completed: 2026-10-13
harness: pi
model: moonshotai/Kimi-K2.6
input_tokens: 33276
output_tokens: 5735
---

# Implement Agreement CRM

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

I wan you to implement the `agreement_crm` module. This modules adds a button "Create
Agreement" to lead form.

When clicking this button an agreement is created. The customer `partner_id` from the
lead is added to the agreement.

The agreement is linked `lead_id` to the lead. Create this field and show it on the form
before `domain`.

## Worklog

Implemented the `agreement_crm` module with the following changes:

- Added `lead_id` Many2one field to `agreement` model.
- Added `action_create_agreement` method to `crm.lead` that creates an agreement with
  the lead's partner and links it back.
- Added `agreement_ids` and `agreement_count` fields to `crm.lead` for smart button
  support.
- Injected a "Create Agreement" button into the CRM lead form header.
- Added a smart button in the lead form's button box to show linked agreements.
- Inherited the agreement form view to show `lead_id` before the `domain` field.
- Added unit tests covering agreement creation, missing partner validation, and
  agreement count.
- All tests pass successfully.

Frontmatter updated with completion details and token counts.
