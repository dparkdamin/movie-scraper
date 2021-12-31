import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import { Button } from 'react-bootstrap';

function App() {

  const [genre, setGenre] = useState("comedy");
  const [count, setCount] = useState(10);
  const movies = [{"title": "hi", "rating": "0"}, {"title": "what", "rating": "2"}]

  const tableData = movies.map((movie) => {
    return <tr>
      <td>{movie.title}</td>
      <td>{movie.rating}</td>
    </tr>
  })

  const getMovies = async values => {
    const params_str = {"movie": values[0], "count": values[1]}
    const params = new URLSearchParams(params_str).toString();
    const server_url = "http://127.0.0.1:8000/" + "?" + params;
    console.log(server_url)
    
    const res = await fetch({
      url: server_url,
      method: "GET",
    });
    const data = await res.json();
    movies = data;
  };

  return (
    
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <div>
        {/* <p>You clicked {count} times</p>
        <button onClick={() => setCount(count + 1)}>
          Click me
        </button> */}

        <select 
          name="genres"
          id="genres"
          defaultValue={genre}
          onChange={(e) => setGenre(e.target.value)}
          >
          <option value="comedy">Comedy</option>
          <option value="sci-fi">Sci-Fi</option>
          <option value="horror">Horror</option>
          <option value="romance">Romance</option>
        </select>
        <select 
        name="count"
        id="count"
        defaultValue={count}
        onChange={(e) => setCount(parseInt(e.target.value, 10))}>
          <option value="10">10</option>
          <option value="25">25</option>
          <option value="50">50</option>
          <option value="100">100</option>
        </select>
        <button onClick={() => getMovies([genre, count])}>
          Submit
        </button>
        
      </div>
      <tbody>
        {tableData}
      </tbody>

    </div>

  );
}

export default App;
