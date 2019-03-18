<template>
	<div class="w-full max-w-lg min-w-sm lg:flex h-64 mb-5
		border border-grey-light rounded  overflow-hidden">
		<div
			v-if="image"
			class="h-48 lg:h-auto text-center lg:w-48 flex-none bg-cover bg-contain bg-no-repeat bg-center"
			:style="background_style">
		</div>
		<div
			class="p-4 flex flex-col justify-between leading-normal">
			<div class="mb-8">
				<a
					target="_blank"
					rel="noopener noreferrer"
					class="text-black no-underline hover:underline font-bold text-xl mb-2"
					:href="card_link">
					{{ heading || 'Loading...' }}
				</a>
				<p class="text-grey-darker text-base" v-html="card_content"></p>
			</div>
		</div>
	</div>
</template>
<script>
export default {
	props: ['heading', 'content', 'image', 'card_link', 'more-link'],
	computed: {
		card_content() {
			return this.content || `Lorem ipsum dolor sit amet, consectetur adipisicing elit.
				Voluptatibus quia, nulla! Maiores et perferendis eaque,
				exercitationem praesentium nihil.`;
		},
		background_style() {
			return `background-image: url(${this.image || 'assets/image-placeholder-1.jpeg'})`;
		}
	}
};
</script>
