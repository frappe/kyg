<template>
	<div>
		<h3>Summary</h3>
		<div v-for="item in items" :key="item">
			<span>{{item.label || 'asd'}}</span>
			<span>{{item.value || 'asfasdf'}}</span>
		</div>
	</div>
</template>
<script>
export default {
	props: ['items']
}
</script>