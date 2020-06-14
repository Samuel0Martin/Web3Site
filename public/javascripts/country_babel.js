let initialPlanets = [];
fetch('http://10.25.138.109/countries')
    .then(response => {
        return response.json();
    }).then(data => {
    initialPlanets = data.results.map((country) => {
        return country
    });
    console.log(initialPlanets);
    this.setState({
		planets: initialPlanets,
    });
});
	
ReactDOM.render(<CountrySearch />, document.getElementById('react-search'));