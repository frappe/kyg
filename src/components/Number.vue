<template>
	<div class="mb-5">
		<div class="w-auto h-32 rounded border border-grey-light p-4">
			<span class="text-grey-dark">{{label}}</span>
			<div class="text-5xl font-bold mt-2">{{value}}</div>
		</div>
	</div>
</template>
<script>
export default {
	props: ['label', 'value']
}
</script>
