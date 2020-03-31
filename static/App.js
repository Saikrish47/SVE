import React, { Component, Fragment } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/layout/Navbar.js';
import Search from './components/user/Search.js';
import Users from './components/user/Users.js';
import User from './components/user/User.js';
import Alert from './components/layout/Alert.js';
import './App.css';
import axios from 'axios';

class App extends Component {
	state = {
		users: [],
		user: {},
		loading: false,
		alert: null
	};

	async componentDidMount() {
		this.setState({ loading: true });
		const res = await axios.get(
			`https://api.github.com/users?client_id=${process.env.REACT_APP_GITHUB_CLIENT_ID}&client_secret=${process.env.REACT_APP_GITHUB_CLIENT_SECRET}`
		);
		this.setState({ users: res.data, loading: false });
	}

	searchUsers = async text => {
		this.setState({ loading: true });
		const res = await axios.get(
			`https://api.github.com/search/users?q=${text}&client_id=${process.env.REACT_APP_GITHUB_CLIENT_ID}&client_secret=${process.env.REACT_APP_GITHUB_CLIENT_SECRET}`
		);
		this.setState({ users: res.data.items, loading: false });
	};

	getUser = async username => {
		this.setState({ loading: true });
		const res = await axios.get(
			`https://api.github.com/search/users/${username}?client_id=${process.env.REACT_APP_GITHUB_CLIENT_ID}&client_secret=${process.env.REACT_APP_GITHUB_CLIENT_SECRET}`
		);
		this.setState({ user: res.data, loading: false });
	};
	clearUsers = () => this.setState({ users: [], loading: false });

	setAlert = (msg, type) => {
		this.setState({ alert: { msg, type } });
		setTimeout(() => this.setState({ alert: null }), 5000);
	};

	render() {
		const { loading, users, user } = this.state;
		return (
			<div className='App'>
				<Router>
					<Navbar title=' github-finder' />
					<div className='container'>
						<Alert alert={this.state.alert} />
						<Switch>
							<Route
								exact
								path='/'
								render={props => (
									<Fragment>
										<Search
											searchUsers={this.searchUsers}
											clearUsers={this.clearUsers}
											showClear={users.length > 0 ? true : false}
											setAlert={this.setAlert}
										/>
										<Users loading={loading} users={users} />
									</Fragment>
								)}
							/>
							<Route
								exact
								path='/user/:login'
								render={props => (
									<Fragment>
										<User
											{...props}
											getUser={this.getUser}
											user={user}
											loading={loading}
										/>
									</Fragment>
								)}
							/>

							<Route exact path='/about' Component={'About'} />
						</Switch>
					</div>
				</Router>
			</div>
		);
	}
}
export default App;
