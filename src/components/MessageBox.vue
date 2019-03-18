<template>
	<div >
		<h3>{{label}}</h3>
		<p class="text-grey-dark">{{content}}</p>
	</div>
</template>
<script>
export default {
	props: ['label', 'content']
}
</script>