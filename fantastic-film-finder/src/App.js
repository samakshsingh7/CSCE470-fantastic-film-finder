import logo from './logo.svg';
import './App.css';
import React, { Component, useEffect, useState } from "react";
import { BrowserRouter, Route, Routes, Link, useLocation } from 'react-router-dom';
import GridLayout from "react-grid-layout";
import styled from "styled-components";
import { Responsive, WidthProvider } from "react-grid-layout";
import Navbar from 'react-bootstrap/Navbar'
import ReactBootstrap, {Nav, Container, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';


const ResponsiveGridLayout = WidthProvider(Responsive);



function Navigation() {
  const location = useLocation();
  const [url, setUrl] = useState(null);
  useEffect(() => {
    setUrl(location.pathname);
  }, [location]);
  return (
    <Navbar bg="dark" variant="dark">
      <Navbar.Brand href="/">Fantastic Film Finder</Navbar.Brand>
      <Nav className="ms-auto">
        <Nav.Link href="/" className={"underline" + (url === "/" ?" active" : "")}>Home</Nav.Link>
        <Nav.Link href="/search" className={"underline" + (url === "/search" ?" active" : "")}>Search by Name</Nav.Link>
        <Nav.Link href="/grid" className={"underline" + (url === "/grid" ?" active" : "")}>Search by Genre</Nav.Link>
      </Nav>
    </Navbar>
  );
}


const layout = [
  { i: "Comedy", x: 0, y: 0, w: 1, h: 1 },
  { i: "Action", x: 1, y: 0, w: 1, h: 1 },
  { i: "t", x: 2, y: 0, w: 1, h: 1 },
  { i: "y", x: 3, y: 0, w: 1, h: 1 },
  { i: "u", x: 4, y: 0, w: 1, h: 1 },
  { i: "6", x: 5, y: 0, w: 1, h: 1 }
];

const GridItemWrapper = styled.div`
  background: #f5f5f5;
  
  
`;

const GridItemContent = styled.div`
  padding: 8px;
  
  
  
`;


const Root = styled.div`
  padding: 16px; 
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  
  
  
  font-size: calc(10px + 2vmin);
`
;

const Grid = () => {
  return (
    <>
      <Navigation/>
      <Root>
        <ResponsiveGridLayout
        layouts={{ lg: layout }}
        breakpoints={{ lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }}
        cols={{ lg: 6, md: 5, sm: 4, xs: 3, xxs: 1 }}
        rowHeight={300}
        width={1200}
        >
          <GridItemWrapper key="Comedy">
            <GridItemContent>Comedy</GridItemContent>
          </GridItemWrapper>
          <GridItemWrapper key="Action">
            <GridItemContent>Action</GridItemContent>
          </GridItemWrapper>
          <GridItemWrapper key="t">
            <GridItemContent>Drama</GridItemContent>
          </GridItemWrapper>
          <GridItemWrapper key="y">
            <GridItemContent>Animation</GridItemContent>
          </GridItemWrapper>
          <GridItemWrapper key="u">
            <GridItemContent>Documentary</GridItemContent>
          </GridItemWrapper>
          <GridItemWrapper key="6">
            <GridItemContent>Short</GridItemContent>
          </GridItemWrapper>
        </ResponsiveGridLayout>
      </Root>
    </>
  );
};

class FlavorForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: 'coconut'};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {    this.setState({value: event.target.value});  }
  handleSubmit(event) {
    alert('Your favorite flavor is: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <div className="App">
      <header className="App-header">
      <form onSubmit={this.handleSubmit}>
       <div class="search-bar">
        <label class="search-label">
               
             <input type="text" name="name" />
           </label>
         <input type="submit" value="Submit" />
         </div>
         <label>
          Search by:
          <select value={this.state.value} onChange={this.handleChange}>            <option value="Title">Title</option>
            {/* <option value="Title">Title</option> */}
            <option value="Director">Director</option>
            <option value="Actor">Actor</option>
          </select>
        </label>
        <input type="submit" value="Submit" />
      </form>
        </header>
    </div>
    );
  }
}

const Search = () => {
  return (
    <>
      <Navigation />
      <FlavorForm></FlavorForm>
    </>
  );
};

const Home = () => {
  return(
    <>
      <Navigation />
      <div className="jumbotron text-center">
          {/* <img src={logo} className="App-logo" alt="logo" /> */}
          <div class="Search-Genre-Name">
            <a class ="Search-Name" href="/search">
              Search by Name
            </a>
            </div>
            <div class="Search-Genre-Div">
            <a class="Search-Genre" href="/grid">
              Search by Genre
            </a>
          </div>
        </div>
    </>
  );
};

class App extends Component {
  render() {
    return (
      //may need to run the following command
      //npm install react-grid-layout
      //displayes genre page
      //Grid()

      //displays search page
      //search_page()

      //home_page()
      <BrowserRouter>
        <div>
          <Routes>
            <Route exact path="/" element={<Home/>} />
            <Route path="/search" element={<Search/>} />
            <Route path="/grid" element={<Grid/>} />
          </Routes>
        </div>
    </BrowserRouter>
    );
  }
}

export default App;
