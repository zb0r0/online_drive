import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Profile = () => {
  const [user, setUser] = useState({
    username: '',
    email: '',
    premium: false
  });

  useEffect(() => {
    // Pobranie informacji o użytkowniku
    axios.get('/api/user')
      .then(response => {
        setUser(response.data);
      })
      .catch(err => {
        console.error("Error fetching user data", err);
      });
  }, []);

  const handleBuyPremium = () => {
    axios.post('/api/buy_premium')
      .then(response => {
        window.location.href = response.data.redirectUrl;
      })
      .catch(err => {
        console.error("Error buying premium", err);
      });
  };

  return (
    <div>
      <h2>Hello, {user.username}</h2>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
      <p>Premium: {user.premium ? 'Yes' : 'No'}</p>
      {user.premium ? (
        <p>You are a premium member!</p>
      ) : (
        <button onClick={handleBuyPremium} className="btn btn-primary">Buy Premium</button>
      )}
    </div>
  );
};

export default Profile;
