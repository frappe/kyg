<template>
	<div id="app">
		<h1 class="py-5">Know Your Government</h1>
		<home></home>
	</div>
</template>

<script>
import Home from './pages/Home.vue';
import './style.css';

export default {
	name: 'app',
	components: {
		Home
	}
};
</script>

<style>
#app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}
</style>
