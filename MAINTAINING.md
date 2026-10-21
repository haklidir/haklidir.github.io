# Siteyi güncel tutma

Site [HugoBlox](https://hugoblox.com) ile Hugo üzerinde kuruludur. `main` dalına her push'ta
GitHub Actions siteyi derler ve GitHub Pages'e yayınlar (Settings → Pages → Source: **GitHub Actions**).

## Nerede ne var

| Ne | Dosya | Nasıl |
|---|---|---|
| Yayınlar | `source/publications.yaml` | Düzenle, sonra betiği çalıştır |
| Araştırma alanları | `source/research_areas.yaml` | Düzenle, sonra betiği çalıştır |
| Konuşmalar | `source/talks.yaml` | Düzenle, sonra betiği çalıştır |
| TV, video, basın | `source/media.yaml` | Düzenle, sonra betiği çalıştır |
| Google Scholar sayıları (atıf, h-index, i10) | `source/metrics.yaml` | Düzenle, sonra betiği çalıştır |
| Profil, biyografi, deneyim, ödüller | `data/authors/me.yaml` | Doğrudan düzenle |
| Ana sayfa düzeni | `content/_index.md` | Doğrudan düzenle |
| Haberler | `content/blog/<klasör>/index.md` | Yeni klasör aç |
| Service, Experience sayfaları | `content/service.md`, `content/experience.md` | Doğrudan düzenle |
| Menü, Analytics, site adı | `config/_default/menus.yaml`, `params.yaml` | Doğrudan düzenle |

`content/publications/`, `content/events/` ve `content/research/` klasörleri betik tarafından
üretilir; elle düzenlemeyin, değişiklik bir sonraki çalıştırmada kaybolur.

```bash
python3 scripts/generate_content.py   # PyYAML gerekir: pip install pyyaml
```

## Yeni yayın eklemek

1. `source/publications.yaml` içine yeni bir kayıt ekleyin (dosyanın başındaki alan listesine bakın).
   `slug` benzersiz olmalı; `authors` listesinde kendiniz için `me` yazın.
2. Özet (abstract) yalnızca makalenin resmi özeti ise `abstract` alanına girer. Kendi kısa
   açıklamanız `overview` alanına yazılır.
3. Ana sayfada öne çıksın istiyorsanız `featured: true`.
4. Betiği çalıştırın, commit edip push edin.

**PDF eklemek:** yayımlanma hakkınız olan sürümü (preprint, kabul edilmiş makale) betiği bir kez
çalıştırdıktan sonra `content/publications/<slug>/<slug>.pdf` olarak koyun. Sayfadaki PDF düğmesi ve
Google Scholar `citation_pdf_url` etiketi bu dosyayı otomatik kullanır. Betik bu dosyaları silmez.

## Haber eklemek

`content/blog/2026-11-kisa-ad/index.md`:

```markdown
---
title: Başlık
summary: Liste görünümünde çıkan bir cümle.
date: 2026-11-05
authors: [me]
tags: [Agentic AI Safety]
---

Metin. Yayına bağlantı: [başlık](/publications/<slug>/)
```

`tags` değerleri `source/research_areas.yaml` içindeki `tag` alanlarıdır.

## Google Scholar

Her yayın sayfasında Highwire `citation_*` meta etiketleri bulunur
(`layouts/_partials/hooks/head-end/scholar-meta.html`). Scholar'ın bir sayfayı dizine alması için
sayfada makalenin özeti veya tam metni olmalıdır; bu yüzden resmi özetleri ve izin verilen PDF'leri
eklemek görünürlüğü en çok artıran adımdır. Yeni sayfaların Scholar'da görünmesi birkaç hafta sürebilir.

## Yerelde önizleme (isteğe bağlı)

Hugo **0.162.0 extended** (sürüm `hugoblox.yaml` ile aynı olmalı), Go, Node.js ve pnpm gerekir.

```bash
pnpm install
hugo server
```

## Site düzeyindeki şablon değişiklikleri

- `layouts/single.html`: yalnızca yılı bilinen yayınlarda sadece yılı gösterir; özeti tam genişlikte gösterir.
- `layouts/_partials/functions/build_links.html`: HugoBlox'taki bir derleme hatasının tek satırlık düzeltmesi.
- `layouts/_partials/hbx/blocks/media-grid/block.html`: Talks & Media sayfasındaki video ve basın kartları.

HugoBlox sürümü `go.mod` dosyasında sabitlenmiştir. Güncellerken bu üç dosyayı yeni sürümle karşılaştırın.
