import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import Register from './components/Register';
import Login from './components/Login';
import Profile from './components/Profile';
import UploadFile from './components/UploadFile';
import BuyPremium from './components/BuyPremium';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" exact component={HomePage} />
                <Route path="/register" component={Register} />
                <Route path="/login" component={Login} />
                <Route path="/profile" component={Profile} />
                <Route path="/upload" component={UploadFile} />
                <Route path="/buy_premium" component={BuyPremium} />
            </Routes>
        </Router>
    );
}

export default App;
