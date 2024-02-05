// Import necessary modules and components
import React, { useState, useEffect } from 'react';
import ReactPlayer from 'react-player';
import axios from 'axios';

import './App.css';

function App() {
  const [overlays, setOverlays] = useState([]);
  const [url, setUrl] = useState('');
  const [videoSize, setVideoSize] = useState({ width: '100%', height: 'auto' });
  const [playing, setPlaying] = useState(false);
  const [volume, setVolume] = useState(0.5);

  useEffect(() => {
    // Fetch overlays from the API
    axios.get('/api/overlays')
      .then(response => setOverlays(response.data))
      .catch(error => console.error('Error fetching overlays:', error));
  }, []);

  const handleOverlayChange = (overlayId, newData) => {
    // Update overlay on the backend
    axios.put(`/api/overlays/${overlayId}`, newData)
      .then(response => console.log(response.data))
      .catch(error => console.error('Error updating overlay:', error));
  };

  const handleUrlChange = (newUrl) => {
    setUrl(newUrl);
  };

  const handlePlayPause = () => {
    // Logic to play or pause the video
    setPlaying(!playing);
  };

  const handleVolumeChange = (newVolume) => {
    // Logic to change the volume
    setVolume(parseFloat(newVolume));
  };

  return (
    <div className="app-container">
      <h1 className="main-heading">Live Stream App</h1>

      <div className="video-container" style={videoSize}>
        <ReactPlayer
          url={url}
          playing={playing}
          controls={false}
          volume={volume}
          width="100%"
          height="100%"
          onPlay={handlePlayPause}
          onPause={handlePlayPause}
          onVolumeChange={handleVolumeChange}
        />
        {overlays.map(overlay => (
          <div
            key={overlay._id}
            className="overlay"
            style={{
              position: 'absolute',
              left: `${overlay.position.x}%`,
              top: `${overlay.position.y}%`,
              width: `${overlay.size.width}%`,
              height: `${overlay.size.height}%`,
              zIndex: 1,
            }}
          >
            {overlay.content}
          </div>
        ))}
      </div>

      <div className="url-input-container">
        <label htmlFor="rtspUrl">RTSP URL:</label>
        <input
          type="text"
          id="rtspUrl"
          value={url}
          onChange={(e) => handleUrlChange(e.target.value)}
        />
      </div>

      {/* Add play and volume buttons after the URL */}
      {url && (
        <div className="playback-buttons">
          <button onClick={handlePlayPause}>{playing ? 'Pause' : 'Play'}</button>
          <button onClick={() => handleVolumeChange(volume + 0.1)}>Increase Volume</button>
          <button onClick={() => handleVolumeChange(volume - 0.1)}>Decrease Volume</button>
        </div>
      )}

      {/* Add overlay form and logic here */}

    </div>
  );
}

export default App;
