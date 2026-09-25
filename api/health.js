export default function handler(req, res) {
  res.setHeader('Cache-Control', 'public, max-age=60, s-maxage=3600');
  res.status(200).json({
    status: 'ok',
    app: 'डिजिटल गुरु (Digital Guru)',
    version: '2.0.0',
    grades: ['Class 6 Mathematics', 'Class 9 Science & Technology'],
    serverEngine: 'Vercel Edge & Node.js High-Performance Server',
    features: {
      brotliCompression: true,
      gzipCompression: true,
      immutableAssetCache: true,
      edgeCacheStaleWhileRevalidate: true,
      pwaOfflineReady: true
    },
    timestamp: new Date().toISOString()
  });
}
