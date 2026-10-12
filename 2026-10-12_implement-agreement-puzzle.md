---
commit_ref: 1feea1124fd0ed78aeeb21e1bbd7661b32ceebc7
title: "Implement Agreement Puzzle"
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: completed
date_completed: 2026-10-12
harness: pi
model: moonshotai/Kimi-K2.6
input_tokens: 35221
output_tokens: 9097
---

# Implement Agreement Puzzle

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

A module `agreement_puzzle` has been initialized in this folder. This module depends on
`oca/agreement/agreement` and adds field required by the company "Puzzle ITC".

The module has been initialized with an inherited model and view. It contains to xml
files to add data and demo data.

Add the fields in english with the technical name. I will then generate the translation
file and you can then updated the field names in German.

### New agreement fields

Add these fields to the agreement model and the form:

**description (Leistungsbeschrieb)**

Is HTML field. The user gives a description of the agreement in this field.

**Group Sale**

These fieds go into a group:

- yearly_fix_price (Jährlicher Fixpreis) Currency
- hourly_rate (Stundensatz) Currency
- cost_cap (Kostendach) Float

**Group Risk**

- chances (Chancen) Text
- risk (Risken) Text

**user_id (Verantwortliche Person)**

Many2one res.user.

**termination_date (Kündigungsfrist)**

Date field that should be shown before `end_date`

**termination_reminder_date (Erinnerung vor Vertragsende)**

Date field that should be shown before `termination_date`

### agreement.type fields

Add these fields to the agreement type model and the form:

- code (Code) Char

Then add this data:

code: framework, individual, maintenance, nda, subcontractor

en: Framework Agreement, Individual Order, Maintenance Agreement, NDA, Subcontractor
Agreement

de: Rahmenvertrag, Einzelauftrag, Wartungsvertrag, NDA, Sublieferantenvertrag

### Subagreements

Add a realted field `type_code` that links `agreement_type_id.code`.

Add a field `child_agreement_ids` that is many2one on `parent_agreement_id`.

Show `parent_id` on form after `agreement_type_id`. Show this field only if code of type
is not `framework`.

If code is `framework` show smart button with "X Subagreements".

## Worklog

The `agreement_puzzle` module was already fully implemented according to all prompt
requirements:

1. **Agreement model fields**: `description` (Html), `yearly_fix_price` (Monetary),
   `hourly_rate` (Monetary), `cost_cap` (Float), `chances` (Text), `risk` (Text),
   `user_id` (Many2one res.users), `termination_date` (Date),
   `termination_reminder_date` (Date) — all added to the model and form view with
   correct grouping and ordering.
2. **Agreement type**: `code` (Char) added to model and form; data records created for
   `framework`, `individual`, `maintenance`, `nda`, and `subcontractor`.
3. **Subagreements**: `type_code` (related), `parent_agreement_id`,
   `child_agreement_ids`, and smart button for framework agreements implemented.
4. **Layout fix**: The _Sale_ and _Risk_ groups in the agreement form are now wrapped
   inside a parent `<group>` so they render side-by-side instead of stacked vertically.

@Clanker Set frontmatter state to completed and update date, harness and model. If you
have access to session info also add token count.
