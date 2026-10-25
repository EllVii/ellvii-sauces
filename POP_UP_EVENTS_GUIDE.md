# Ell Vii's Sauces pop-up schedule

The pop-up tasting and hot challenge page is at /pop-ups.html. The storefront links to it.

## Publishing an event
Edit BOTH \`data/popups.json\` and \`public/data/popups.json\` with the same contents. The root copy supports static publishing and the public copy supports Create React App builds. Add an item to the \`events\` array **only after location, timing, and permission to announce are confirmed**:

\`\`\`json
{
  "timeZone": "America/Phoenix",
  "events": [
    {
      "id": "unique-event-id",
      "title": "Ell Vii's Sauces pop-up tasting",
      "date": "2026-11-14",
      "time": "1:00 PM - 4:00 PM",
      "venue": "CONFIRMED VENUE NAME",
      "address": "CONFIRMED STREET ADDRESS, CITY, AZ ZIP",
      "description": "Salsa tasting; optional hot challenge details announced on-site.",
      "lat": null,
      "lng": null,
      "status": "published"
    }
  ]
}
\`\`\`

**The date, time, and venue above are illustrative placeholders. Do not publish them as a real event.** Replace all fields with verified details. Add accurate numeric latitude and longitude to place a map pin; if coordinates are unknown, leave null and the event card still provides Google Maps directions by address. Events dated before the current Arizona date are automatically excluded. To hide an event early, set its status to \`draft\`.

The map uses Leaflet and OpenStreetMap tiles; no API key. It starts at a general Arizona/Phoenix-area view and shows **no event pin** unless a published event with coordinates is provided. A link for new event details is generated from the verified address.

## Interest form & filming
The interest form opens a local email draft addressed to ellviisauces@gmail.com. **No data is stored or transmitted by the site.** A visitor must send the message in their own email app. No booking or confirmation is created. To accept submissions directly on the site later, create a secured server-side form handler with spam protection, privacy disclosures and consent logging.

Instagram/Facebook and YouTube checkboxes mean interest in being considered, **not consent**. Obtain separate voluntary, documented filming/publication permissions before posting; minors require guardian authorization. Participation does not depend on agreeing to appear in media. Do not add an unverified YouTube channel URL. The adults-only challenge is optional and not guaranteed at every location.

## Deployment note
The repository maintains matching top-level and \`public/\` versions of static pages. Both are updated to support either static-root deployments or builds that copy \`public/\` to their output. Verify deployment configuration and the live /pop-ups.html route after merging.
