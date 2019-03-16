<template>
	<div v-if="filtered_items && filtered_items.length" class="border-r-2 w-48">
		<a
			class="list-reset p-3 flex flex-col cursor-pointer"
			:class="{ 'bg-blue hover:bg-blue': index === selected }"
			v-for="(item, index) in filtered_items"
			:key="index" @click="$emit('item_clicked', index)">{{ item.label || item }}
		</a>
	</div>
</template>
<script>
export default {
	props: ['items', 'selected'],
	computed: {
		filtered_items() {
			if (!this.items) return []
			if (Array.isArray(this.items)) {
				return this.items;
			} else {
				return Object.keys(this.items)
			}
		}
	}
}
</script>