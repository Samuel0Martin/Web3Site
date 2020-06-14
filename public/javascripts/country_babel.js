class CountrySearch extends Component {
    constructor() {
        super();
        this.state = {
            planets: [],
        };
    }
}

componentDidMount() {
    let initialPlanets = [];
    fetch('https://swapi.co/api/planets/')
        .then(response => {
            return response.json();
        }).then(data => {
        initialPlanets = data.results.map((planet) => {
            return planet
        });
        console.log(initialPlanets);
        this.setState({
            planets: initialPlanets,
        });
    });
}
	
ReactDOM.render(<CountrySearch />, document.getElementById('react-search'));