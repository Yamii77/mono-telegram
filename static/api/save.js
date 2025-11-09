export default async function handler(req, res) {
  if (req.method === 'POST') {
    const body = await req.json();
    console.log('Progress saved:', body);
    return res.status(200).json({ ok: true });
  }
  return res.status(405).json({ error: 'Method not allowed' });
}
