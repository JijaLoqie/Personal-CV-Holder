import React from "react";
import { render } from "react-dom";

import { BrowserRouter, Routes, Route } from "react-router-dom"
import HomePage from './HomePage';
import CreatePage from './CreatePage';
import UpdatePage from './UpdatePage';


export default App = () => {
    return (
      <div>
        <BrowserRouter basename="/">
          <Routes>
            <Route path="home" element={<HomePage/>} />
            {/* 👈 Renders at /app/hello */}
            <Route exact path="create" element={<CreatePage/>} />
            {/* 👈 Renders at /app/what */}
            <Route exact path="update" element={<UpdatePage/>} />
            {/* 👈 Renders at /app/hello */}
          </Routes>
        </BrowserRouter>
      </div>
    );
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
