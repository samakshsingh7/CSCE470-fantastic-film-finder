import logo from './logo.svg';
import './genres.css';
import React, { Component } from "react";
import GridLayout from "react-grid-layout";
import styled from "styled-components";
import { Responsive, WidthProvider } from "react-grid-layout";
const ResponsiveGridLayout = WidthProvider(Responsive);


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

export const Grid = () => {
  return (
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

export const search_page = () => {
  return (
    
    <FlavorForm></FlavorForm>
  );
};

function App() {
  return (
    //may need to run the following command
    //npm install react-grid-layout
    //displayes genre page
    Grid()

    //displays search page
    // search_page()

    // home page
    // <div className="App">
    //   <header className="App-header">
    //     <text class = "index-title">Fantastic Film Finder</text>
    //     {/* <img src={logo} className="App-logo" alt="logo" /> */}
    //     <div class="Search-Genre-Name">
    //     <a class ="Search-Name">
    //       Search by Name
    //     </a>
    //     </div>
    //     <div class="Search-Genre-Div">
    //     <a class="Search-Genre">
    //       Search by Genre
    //     </a>
    //     </div>
        
    //   </header>
    // </div>
  
  );
}

export default App;