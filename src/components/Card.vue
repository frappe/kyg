<template>
	<div class="max-w-md w-full lg:flex h-64">
		<div
			v-if="image"
			class="h-48 lg:h-auto lg:w-48 flex-none bg-cover rounded-t
				lg:rounded-t-none lg:rounded-l text-center overflow-hidden bg-center"
			:style="background_style">
		</div>
		<div
			class="border-r border-b border-l border-grey-light
			lg:border-l-0 lg:border-t lg:border-grey-light
			bg-white rounded-b lg:rounded-b-none lg:rounded-r
			p-4 flex flex-col justify-between leading-normal">
			<div class="mb-8">
				<div class="text-black font-bold text-xl mb-2">{{heading}}</div>
				<p class="text-grey-darker text-base">
					Lorem ipsum dolor sit amet, consectetur adipisicing elit.
					Voluptatibus quia, nulla! Maiores et perferendis eaque,
					exercitationem praesentium nihil.
				</p>
			</div>
		</div>
	</div>
</template>
<script>
export default {
	props: ['heading', 'content', 'image', 'more-link'],
	data() {
		return {
			background_style: `background-image: url(${this.image})`
		}
	}
};
</script>
