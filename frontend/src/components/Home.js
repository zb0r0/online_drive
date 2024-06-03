import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Home = () => {
  const [files, setFiles] = useState([]);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Sprawdzenie czy użytkownik jest zalogowany
    axios.get('/api/check_auth')
      .then(response => {
        setIsAuthenticated(response.data.isAuthenticated);
        if (response.data.isAuthenticated) {
          // Pobranie plików użytkownika
          axios.get('/api/files')
            .then(res => {
              setFiles(res.data.files);
            })
            .catch(err => {
              console.error("Error fetching files", err);
            });
        }
      })
      .catch(err => {
        console.error("Error checking auth", err);
      });
  }, []);

  const handleDelete = (fileId) => {
    axios.post(`/api/delete/${fileId}`)
      .then(response => {
        // Aktualizacja listy plików po usunięciu
        setFiles(files.filter(file => file.id !== fileId));
      })
      .catch(err => {
        console.error("Error deleting file", err);
      });
  };

  return (
    <div>
      <h1>Welcome to the Home Page</h1>
      {isAuthenticated ? (
        <>
          <h2>Your Files:</h2>
          <ul>
            {files.map(file => (
              <li key={file.id}>
                <a href={`/api/uploads/${file.filename}`}>{file.filename}</a>
                <button
                  onClick={() => handleDelete(file.id)}
                  className="btn btn-danger btn-sm"
                  style={{ display: 'inline', marginLeft: '10px' }}
                >
                  Delete
                </button>
              </li>
            ))}
          </ul>
          <Link to="/upload">Upload New File</Link>
        </>
      ) : (
        <p>Please <Link to="/login">log in</Link> to see your files.</p>
      )}
    </div>
  );
};

export default Home;
