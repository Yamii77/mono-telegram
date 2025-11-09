export default async function handler(req, res) {
  const { userId } = req.query;
  console.log('Progress loaded for:', userId);
  return res.status(200).json({ 
    score: 0, streak: 0, totalCards: 0, lastWordIndex: -1 
  });
}
