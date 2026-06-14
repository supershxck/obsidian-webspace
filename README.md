# Obsidian Webspace

> Publish an Obsidian vault as a browsable static website — Nginx, JS, and Python tooling.

| | |
|---|---|
| **Status** | MVP — vault-to-web pipeline works |
| **Stack** | JavaScript, Python, Nginx, Docker |
| **Repo** | [supershxck/obsidian-webspace](https://github.com/supershxck/obsidian-webspace) |

## Purpose

Self-hosted alternative to Obsidian Publish: turn a markdown vault into HTML pages with interactivity. Pairs with `obsidian-ruby-viewer` (search, graph, export) as a future merged product.

## Current state

- Full vault export under `html/` and `obsidian-vault/`
- JS, Python, Ruby, and Nginx serving layers
- Docker-ready deployment path

## Work in progress

- [ ] Merge best features with `obsidian-ruby-viewer`
- [ ] Backlink graph and full-text search
- [ ] Auth for private vs public notes
- [ ] Single-image Docker packaging

## Quick start

See `nginx/` and Docker configs in repo root. Point Nginx at generated `html/` output after running the Python/JS publish scripts.

**Note:** Large personal vault content may be present locally — review before making repo public.